
/*
console.log('Hello!!')
var password = prompt('Password');
alert('Hello '+name);
if (password=='123') {
  alert('OK');
} else {
  alert('NOT OK');
}

el = $('#mi').hide();

var el = document.getElementById('mi');
// console.log(el);

var btn = $('#mybutton');
btn.on('click',() => {
    // var mt = $('#mt').val();
    // $('#mycontent').html(mt); 
    $('#userlist').append('<tr><td>gggggg</td></tr>');
});

*/

/*
// формируем новые поля
jQuery('.plus').click(function(){
	jQuery('.information_json_plus').before(
	'<tr>' +
		'<td><input type="text" class="form-control" name="information_json_name[]" placeholder="Название поля"></td>' +
		'<td><input type="text" class="form-control" name="information_json_val[]" placeholder="Значение поля"></td>' +
		'<td><span class="btn btn-danger minus pull-right">&ndash;</span></td>' +
	'</tr>'
	);
});
// on - так как элемент динамически создан и обычный обработчик с ним не работает
jQuery(document).on('click', '.minus', function(){
	jQuery( this ).closest( 'tr' ).remove(); // удаление строки с полями
});
*/





/* (HTML таблица, можно без JS) Добавление, редактирование данных в таблице, до обнавления*/


/* (таблица Students) Добавление, редактирование данных в таблице, до обнавления*/
function addRow(){
	//введённые "массивы"
	var fname = document.getElementById('fname').value;
	var lname = document.getElementById('lname').value;
	var rname = document.getElementById('rname').value;

	//Html таблица | 0 = первое значение
	var table = document.getElementsByTagName('table')[0];

	//добавить новую запись в таблицу
	//сортировка 1 - первый, последний - table.rows.length
	var newRow = table.insertRow(1);	
			
	
	var cel1 = newRow.insertCell(0);
	var cel2 = newRow.insertCell(1);
	var cel3 = newRow.insertCell(2);

	cel1.innerHTML = fname;
	cel2.innerHTML = lname;
	cel3.innerHTML = rname;
}






/* (последняя таблица) Добавление, редактирование данных в таблице, до обнавления*/

var tds = document.querySelectorAll('td');

for (var i = 0; i < tds.length; i++) {
	tds[i].addEventListener('click', function func() {
		var input = document.createElement('input');
		input.value = this.innerHTML;
		this.innerHTML = '';
		this.appendChild(input);

		var td = this;
		input.addEventListener('blur', function(){
			/* очистка ячейки */
			td.innerHTML = this.value;
			/* двойной клик - редактирование */
			td.addEventListener('click', func);
		});
		
		this.removeEventListener('click', func);
	});
}










