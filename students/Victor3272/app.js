document.getElementById('average').addEventListener('submit', function (event) {
    event.preventDefault();
    
    var tr = document.createElement("tr");
    var cols = ['nam', 'prof', 'rating'];
    
      for (var q=0; q<cols.length; ++q) {
    var td = document.createElement("td");
    td.textContent = document.getElementById(cols[q]).value;
    tr.appendChild(td);
  }
    document.getElementById('dest').appendChild(tr);
  });

  

