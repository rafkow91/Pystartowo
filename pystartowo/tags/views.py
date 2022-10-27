from dal import autocomplete
from tags.models import Tag


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Tag.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs
