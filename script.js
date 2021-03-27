$(document).ready(function() {
    var dataset = ["["];

    $.getJSON("objects.json", function( data ) {

        $.each( data, function( key, val ) {

            dataset += '[';
            dataset +=" '"+val.name+"',";
            dataset += " '"+val.position+"',";
            dataset += " '"+val.office+"',";
            dataset += " '"+val.extn+"',";
            dataset += " '"+val.start_date+"',";
            dataset += " '"+val.salary+"'";
            dataset += '],'; 

        });
        dataset= dataset.slice(0, -1);
        dataset += ']';
            console.log(dataset);

            $('#example').DataTable({
data: dataset,
columns: [
    { title: "Name" },
    { title: "Position" },
    { title: "Office" },
    { title: "Extn." },
    { title: "Start date" },
    { title: "Salary" }]

});
         
          
});

    

});
