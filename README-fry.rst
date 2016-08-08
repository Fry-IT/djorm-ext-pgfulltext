29.1.2016 - 0.9.1-1-fry
=======================

 * Removed db_index=True from VectorField. If db_index=False is passed to field,
   the index has to be created manually as a GIN type, for example
   CREATE INDEX table_search_index ON table USING gin(search_index)
   See also
   https://github.com/linuxlewis/djorm-ext-pgfulltext/issues/45
   https://github.com/linuxlewis/djorm-ext-pgfulltext/issues/14

5.8.2016 - 0.9.3-1-fry
======================

 * Merged with upstream 0.9.3 tag to get Django 1.8 compatibility
   We still use some custom behavior.

8.8.2016 - 0.9.3-2-fry
======================

 * Added missing parameter for update index function
