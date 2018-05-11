## tools-that-love

### Summary

A dataset of pairwise popularity of research tools.

Data is taken from the first worksheet.

* Writeup: https://101innovations.wordpress.com/2016/11/06/tools-that-love-to-be-together/
* Source: https://docs.google.com/spreadsheets/d/1d2YSAmYGEw1WTMHk2Wfz-L155bjxT6eQkO772FJko8E/edit#gid=1535973383
* Authors: [@bmkramer](https://github.com/bmkramer), [@JeroenBosman](https://github.com/@JeroenBosman)


### Files

#### providers.txt

Format: tab-separated file, `\n` line endings

Columns:

* `id`: id number for the provider
* `category_tag`: a short category identifier
* `category_name`: a human readable name for the category
* `provider`: name of the provider

Notes:

* `provider` is not unique with in the column.  Some providers might server more than one function.
* `category_tag` and `category_name` map 1-to-1.


#### provider-interactions.txt

Format: tab-separated file, `\n` line endings

Columns:

* `id`: id number for the provider
* `category_tag`: a short category identifier
* `category_name`: a human readable name for the category
* `provider`: name of the provider
* `id_$i`: interaction of the provider with the provider with `id == $i`

Notes:

* *The first four columns are identical to those in `providers.txt`.*
* `provider` is not unique with in the column.  Some providers might server more than one function.
* `category_tag` and `category_name` map 1-to-1.
* `id_$i`: Four possible values:
  * **NA**: providers are identical
  * **0**: no significant association
  * **1**: positive association between providers
  * **-1**: negative association between providers
