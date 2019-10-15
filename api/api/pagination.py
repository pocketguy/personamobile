from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        next_page_number = None
        previous_page_number = None
        if self.page.has_next():
            next_page_number = self.page.next_page_number()
        if self.page.has_previous():
            previous_page_number = self.page.previous_page_number()
        return Response(
            OrderedDict(
                [
                    ("count", self.page.paginator.count),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("total_pages", self.page.paginator.num_pages),
                    ("current_page", self.page.number),
                    ("next_page_number", next_page_number),
                    ("previous_page_number", previous_page_number),
                    ("results", data),
                ]
            )
        )
