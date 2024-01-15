import random
import string

from django_components import component


def get_random_string(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


@component.register("card")
class Card(component.Component):
    template_name = "components/card.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(  # noqa PLR0913
        self, title, color="", text_color="", header_color="", header_text_color="", border_color=""
    ):
        return {
            "title": title,
            "color": color,
            "text-color": text_color,
            "header_color": header_color,
            "header_text_color": header_text_color,
            "border_color": border_color,
        }

    class Media:
        css = ""
        js = ""


@component.register("collapsible-card")
class CollapsibleCard(component.Component):
    # Note that Django will look for templates inside `[your app]/components` dir
    # To customize which template to use based on context override get_template_name instead
    template_name = "components/collapsible-card.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(  # noqa PLR0913
        self, title, color="", text_color="", header_color="", header_text_color="", border_color="", show=False
    ):
        rid = get_random_string(12)

        return {
            "title": title,
            "color": color,
            "text-color": text_color,
            "header_color": header_color,
            "header_text_color": header_text_color,
            "border_color": border_color,
            "rid": rid,
            "show": show,
        }

    class Media:
        css = ""
        js = ""


@component.register("collapsible-filter")
class CollapsibleFilter(component.Component):
    # Note that Django will look for templates inside `[your app]/components` dir
    # To customize which template to use based on context override get_template_name instead
    template_name = "components/collapsible-filter.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(self, title, color="", btn_color="info", border_color="", show=False):  # noqa PLR0913
        rid = get_random_string(12)

        return {
            "title": title,
            "color": color,
            "btn_color": btn_color,
            "border_color": border_color,
            "rid": rid,
            "show": show,
        }

    class Media:
        css = ""
        js = ""
