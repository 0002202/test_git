const modal = document.getElementById("myModal");
const confirmBtn = document.getElementById("confirmBtn");
const cancelBtn = document.getElementById("cancelBtn");

function delQuestion(button){
    // event.preventDefault();     // 阻止事件的默认行为,防止页面自动跳转
    // 将对象事件转换为dom对象
    // var button = event.target;
    // 获取父元素的题号ID
    var QUESTIONID = button.getAttribute('delId');
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


// 打开模态框
function openModal() {
  modal.style.display = "block";
}

// 关闭模态框
function closeModal() {
  modal.style.display = "none";
}

// 处理确认按钮点击事件
function handleConfirmClick() {
  // 点击确认按钮后的处理逻辑
  console.log("确认按钮被点击");
  delQuestion();
  closeModal();
}

// 处理取消按钮点击事件
function handleCancelClick() {
  // 点击取消按钮后的处理逻辑
  console.log("取消按钮被点击");
  closeModal();
}

confirmBtn.addEventListener("click", handleConfirmClick);
cancelBtn.addEventListener("click", handleCancelClick);

function clickDelQuestion(){
    // 打开模态框
    openModal();

}