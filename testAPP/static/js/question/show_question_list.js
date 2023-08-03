function clearTable() {
  var table = document.getElementById("question-table");
  var header_row = table.rows[0];
  table.innerHTML = "";
  table.appendChild(header_row);
}
function search(event) {
    event.preventDefault();             // 阻止默认的表单提交行为
    var input = document.getElementById("search");
    var keyword = input.value;
      // 将数据提交到后端
      $.ajax({
          url: '/question/',
          type: 'GET',
          data: {
              'search_key': keyword,
          },
      })
}

window.onload = function() {
    var search_btn = document.getElementById('search-btn');
    search_btn.addEventListener('click', clearTable);
    search_btn.addEventListener('click', search);
}

