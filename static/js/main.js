// function onClick(element) {
//   document.getElementById("img01").src = element.src;
//   document.getElementById("modal01").style.display = "block";
// }
$('.img-link').click(function(){
  $('#modal-title').html($(this).data('img-name'));
  $('#modal-description').html($(this).data('description'));
  var imgsrc = $(this).data('id');
  $('#my_image').attr('src',imgsrc);
 

  console.log(description);
});
