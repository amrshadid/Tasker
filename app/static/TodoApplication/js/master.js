
function edit(title, content , id,pl){
$(document).ready(function () {
    var url = "/task/edit/" + id.value +"/"+pl.value+"/";
     $('#EditFrom').attr('action', url);
     $("#nik").val(title.value);
     $("#discrption").val(content.value);

   })};
