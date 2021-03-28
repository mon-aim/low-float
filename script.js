$(document).ready(function() {
    var dataset = [];
    $.getJSON("scrape.json", function( data ) {
              
        $.each( data, function( key, val ) {
            var row =[];
            row.push(val.Ticker);
            row.push(val.Company);
            row.push(val.Exchange);
            row.push(val.Float);
            row.push(val.Outstd);
            row.push(val.ShortInt);
            row.push(val.Industry);

            dataset.push(row);
        });

            $('#example').DataTable({
data: dataset,
columns: [
    { title:  "Ticker"},
    { title:   "Company"},
    { title:   "Exchange"},
    { title:  "Float"},
    { title:  "Outstd"},
    { title:  "ShortInt"},
    { title:  "Industry"}
    
    ]

});
         
          
});

    

});
