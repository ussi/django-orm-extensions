# -*- coding: utf-8 -*-

from django_orm.cache.queryset import CachedQuerySet
from django_orm.sqlite3.extra_functions import ensure_sqlite_function

class UnaccentQuerysetMixin(object):
    @ensure_sqlite_function('unaccent')
    def unaccent(self, **kwargs):
        where, params = [], []
        for field, search_term in kwargs.items():
            where_sql = "unaccent(%s) LIKE unaccent(%%s) ESCAPE '\\'" % (field)
            where.append(where_sql)
            params.append(self._prepare_search_term(search_term))

        return self.extra(where=where, params=params)

    def _prepare_search_term(self, term):
        return u"%%%s%%" % term

    iunaccent = unaccent

class SqliteQuerySet(UnaccentQuerysetMixin, CachedQuerySet):
    pass