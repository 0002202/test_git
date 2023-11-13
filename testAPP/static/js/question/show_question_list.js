function delQuestion(button){
    // event.preventDefault();     // 阻止事件的默认行为,防止页面自动跳转
    // 将对象事件转换为dom对象
    // var button = event.target;
    // 获取父元素的题号ID
    var QUESTIONID = button.getAttribute('delId');;
    console.log(QUESTIONID);
    $.ajax({
        url: '/del_question/',
        type: 'POST',
        data: {
            'questionID': QUESTIONID,
        },
        success:function (res){
            if (res.msg === 'success'){
                // 刷新页面
                location.reload();
                console.log('删除成功！');
            }else {
                throw new Error('Question not found');
                // alert('删除失败！请联系管理员。');
            }
        }
        
    })
}