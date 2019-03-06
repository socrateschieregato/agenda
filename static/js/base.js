function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();

    $("#myTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });

  });
});

// Get the Sidebar
var mySidebar = document.getElementById("mySidebar");

// Get the DIV with overlay effect
var overlayBg = document.getElementById("myOverlay");

// Toggle between showing and hiding the sidebar, and add overlay effect
function w3_open() {
    if (mySidebar.style.display === 'block') {
        mySidebar.style.display = 'none';
        overlayBg.style.display = "none";
    } else {
        mySidebar.style.display = 'block';
        overlayBg.style.display = "block";
    }
}

// Close the sidebar with the close button
function w3_close() {
    mySidebar.style.display = "none";
    overlayBg.style.display = "none";
}
// // Datepicker
// $(document).ready(function(){
//     $('#id_validade').datepicker({
//         dateFormat: "dd/mm/yy"
//     });
//
//     $('#id_validade').datepicker(
//         "option", "dayNamesMin", [ "D", "S", "T", "Q", "Q", "S", "S" ]
//     );
//
//     $( "#id_validade" ).datepicker(
//         "option", "monthNames", [ "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" ]
//     );
//
//     $( "#id_validade" ).datepicker(
//         "option", "changeYear", true
//     );
//
//      $( "#id_validade" ).datepicker(
//         "option", "changeMonth", true
//     );
// });