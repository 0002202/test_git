const modal = document.getElementById("myModal");
const confirmBtn = document.getElementById("confirmBtn");
const cancelBtn = document.getElementById("cancelBtn");

const elements = document.querySelectorAll('.delButton');

var QUESTIONID;
// 遍历元素，并为每个元素绑定点击事件监听器
elements.forEach(element => {
  element.addEventListener('click', clickDelQuestion);
  
});


function delQuestion(){
    // event.preventDefault();     // 阻止事件的默认行为,防止页面自动跳转
    // 将对象事件转换为dom对象
    // var button = event.target;
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
  delQuestion(button);
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

// 绑定监听事件
function clickDelQuestion(){
    QUESTIONID = this.getAttribute('delId');
    // 打开模态框
    openModal();

}
console.log(QUESTIONID);