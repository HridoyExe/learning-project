from rest_framework.pagination import PageNumberPagination

class DeafultPaginations(PageNumberPagination):
    page_size = 10