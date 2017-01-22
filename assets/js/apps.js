$(document).ready(function(){
  console.log("we are ready to go");
  function getImage(){
      alert('image viewer button clicked');
  }

  //document.getElementById('id_username').type = 'text';
  //document.getElementById('id_username').setAttribute('class','form-control');
  //document.getElementById('id_password').setAttribute('class','form-control');
  $("#ajax").mouseover(function(){
    //alert('image viewer button clicked');
    var url = "http://0.0.0.0:7000/ajax";
  ;
    var imageurl = "";
    $.ajax({url: url,
      dataType: 'text',
      type: 'GET',
      async: true,
       success: function(result){
      //$("#greatphoto").html(result);

      //alert(imageurl=result);
      $("#greatphoto").attr('src',result);
  }});
  });

});

function getImage(){
    alert('image viewer button clicked');
}
