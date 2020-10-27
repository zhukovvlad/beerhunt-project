from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError, PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse

from .models import Beer, Vote, BeerComment
from .forms import VoteForm


class BeerListView(ListView):
    paginate_by = 10
    # model = Beer
    queryset = Beer.objects.all_with_related_instances_and_score()

    context_object_name = 'beer_list'

    ordering = ['-score']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['total_beer_list'] = Beer.objects.all()
        return context


class BeerDetailView(DetailView):
    queryset = Beer.objects.all_with_related_instances_and_score()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            #   beer_comment = BeerComment(
            #       beer=self.object,
            #       author=self.request.user
            #   )

            vote = Vote.objects.get_vote_or_unsaved_blank_vote(
                beer=self.object,
                user=self.request.user
            )

            if vote.id:
                vote_form_url = reverse(
                    'beer:UpdateVote',
                    kwargs={
                        'beer_id': vote.beer.id,
                        'pk': vote.id
                    }
                )
            else:
                vote_form_url = (
                    reverse(
                        'beer:CreateVote',
                        kwargs={
                            'beer_id': self.object.id
                            })
                )
            vote_form = VoteForm(instance=vote)
            #   beer_comment_form = BeerCommentForm(instance=beer_comment)
            ctx['vote'] = vote
            ctx['vote_form'] = vote_form
            ctx['vote_form_url'] = vote_form_url
            #   ctx['beer_comment_form'] = beer_comment_form
        return ctx


class BeerCreateView(LoginRequiredMixin, CreateView):
    model = Beer
    template_name = "beers/beer_form.html"

    fields = [
        'title',
        'style',
        'description',
        'image',
        'brewery',
        'hops',
        'og',
        'abv',
        'ibu'
    ]

    def form_valid(self, form):
        form.instance.hunter = self.request.user
        return super().form_valid(form)


class CreateVote(LoginRequiredMixin, CreateView):
    form_class = VoteForm

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user.id
        initial['beer'] = self.kwargs['beer_id']
        return initial

    def get_success_url(self):
        beer_slug = self.object.beer.slug
        try:
            return reverse(
                'beer:BeerDetail',
                kwargs={
                    'slug': beer_slug})
        except:
            raise ValidationError("Oooops")

    def render_to_response(self, context, **response_kwargs):
        beer_id = context['object'].id
        beer_detail_url = reverse(
            'beer:BeerDetail',
            kwargs={'pk': beer_id})
        return redirect(
            to=beer_detail_url)


class UpdateVote(LoginRequiredMixin, UpdateView):
    form_class = VoteForm
    queryset = Vote.objects.all()

    def get_object(self, queryset=None):
        vote = super().get_object(queryset)
        user = self.request.user
        if vote.user != user:
            raise PermissionDenied(
                'cannot change another '
                'users vote'
                )
        return vote

    def get_success_url(self):
        beer_slug = self.object.beer.slug
        return reverse(
            'beer:BeerDetail',
            kwargs={'slug': beer_slug})

    def render_to_response(self, context, **response_kwargs):
        beer_id = context['object'].id
        beer_detail_url = reverse(
            'beer:BeerDetail',
            kwargs={'pk': beer_id})
        return redirect(
            to=beer_detail_url)
