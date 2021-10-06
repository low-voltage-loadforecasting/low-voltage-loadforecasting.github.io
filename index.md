---
layout: default
---
# Review of Low-Voltage Load Forecasting
## Read
This is an overview of load forecasting data sets as presented in our paper available as [preprint on arXiv](https://arxiv.org/pdf/2106.00006.pdf) and published in [Applied Energy](https://www.sciencedirect.com/science/article/pii/S0306261921011326).

## Contribute
You know datasets that are missing? See our  [Github repository](https://github.com/low-voltage-loadforecasting/low-voltage-loadforecasting.github.io) of this page on how to contribute!

## Use

<table id="dataset-table">
    <thead>
        <tr class="header">
            <th>Name</th>
            <th>Bibtexkey</th>
			<th>Type</th>
            <th>No. Customers</th>
            <th>Resolution</th>
			<th>Duration</th>
            <th>Intervention</th>
            <th>Sub-metering</th>
			<th>Weather avail.</th>
			<th>Location</th>
            <th>Other data provided:</th>
            <th>Access/Licence</th>
        </tr>
    </thead>
    <tbody>
    {% for entry in site.data.data %}
        <tr>
          <td>  <a href="{{ entry.Url }}">{{ entry.Name }}</a> </td>  
          <td>
			{% if entry.Bibtexkey[0] %}
				{% for key in entry.Bibtexkey %}
					{% cite key %}
				{% endfor %}
			{% else %}
				{% if entry.Bibtexkey %}
					{% cite entry.Bibtexkey %}
				{% endif %}
			{% endif %}
		  </td>
		  <td>{{entry.Type}}</td>
          <td>{{entry.Customers}}</td>
          <td>{{entry.Resolution}}</td>
		  <td>{{entry.Duration}}</td>
          <td>{{entry.Intervention}}</td>
          <td>{{entry.Submetering}}</td>
		  <td>{{entry.Weather}}</td>
          <td>{{entry.Location}}</td>
          <td>{{entry.Other}}</td>
		  <td>{{entry.Licence}}</td>
        </tr>
    {% endfor %}
    </tbody>
</table>

<script>
  $(document).ready( function () {
    $('#dataset-table').DataTable({
            "autoWidth": true,
            "pageLength": 20
        });
} );
</script>

## Cite

If you find it useful and use it in your work, feel free to cite our preprint:

```latex
@article{haben2021review,
    title = {Review of low voltage load forecasting: Methods, applications, and recommendations},
    journal = {Applied Energy},
    volume = {304},
    pages = {117798},
    year = {2021},
    issn = {0306-2619},
    doi = {https://doi.org/10.1016/j.apenergy.2021.117798},
    url = {https://www.sciencedirect.com/science/article/pii/S0306261921011326},
    author = {Stephen Haben and Siddharth Arora and Georgios Giasemidis and Marcus Voss and Danica {Vukadinović Greetham}},
}
```

## References

{% bibliography --cited %}