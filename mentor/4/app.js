// console.log('Hello!!')
// var password = prompt('Password');
// alert('Hello '+name);
// if (password=='123') {
//   alert('OK');
// } else {
//   alert('NOT OK');
// }

// el = $('#mi').hide();

// //var el = document.getElementById('mi');
// console.log(el);

var btn = $('#mybutton');
btn.on('click',() => {
    var mt = $('#mt').val();
    $('#mycontent').html(mt); 
});





