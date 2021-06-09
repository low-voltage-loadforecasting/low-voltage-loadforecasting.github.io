---
layout: default
datatable: true
---
# Review of Low-Voltage Load Forecasting
## Read
This is an overview of load forecasting data sets as presented in our [preprint on arXiv](https://arxiv.org/pdf/2106.00006v1.pdf).

## Contribute
You know datasets that are missing? See our  [Github repository](https://github.com/low-voltage-loadforecasting/low-voltage-loadforecasting.github.io) of this page on how to contribute!

## Use

<table class="display"> 
  {% for row in site.data.datasets %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {{ pair[1] }}
    {% endtablerow %}
  {% endfor %}
</table>

## Cite

If you find it useful and use it in your work, feel free to cite our preprint:

```latex
@misc{haben2021review,
          title={Review of Low-Voltage Load Forecasting: Methods, Applications, and Recommendations}, 
          author={Stephen Haben and Siddharth Arora and Georgios Giasemidis and Marcus Voss and Danica Vukadinovic Greetham},
          year={2021},
          eprint={2106.00006},
          archivePrefix={arXiv},
          primaryClass={stat.OT}
}
```