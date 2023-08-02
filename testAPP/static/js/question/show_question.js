// 通过判断题目类型将复选框进行禁用
function IsDocumentCheckbox(){
    // 获取题目类型
    var con_type = document.querySelector('.content_type').innerText;
    if (con_type === '单选选择'){
        // 将其余checkbox设置为禁用

    }
}


function GetDocumentCheck(checkBox) {
    var content = document.querySelector('.content').innerText;
    var checkboxes = document.getElementsByClassName('checkbox');
    var options = document.getElementsByClassName('checkbox-label');
    for (var i = 0; i < checkboxes.length; i++) {
        // 考虑点击后的获取数据
        checkboxes[i].addEventListener('click', function (){
            if(this.checked){
                var text = this.nextElementSibling.innerText;       // 若是多选题，则应返回多个选项
                // 将数据提交到后端
                $.ajax({
                    url: '/is_correct/',
                    type: 'POST',
                    data: {
                        'content': content,
                        'option': text,
                    },
                    success:function (res){
                        if (res.msg === 'success'){
                            // 对数据进行判断，或者当答题成功后，将页面继续沿着下一题
                            alert('回答正确');
                        }else {
                            alert('回答错误');
                        }
                    }
                })
            }
        })
    }
}


window.onload = function() {
    GetDocumentCheck();
}