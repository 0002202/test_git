const modal = document.getElementById("myModal");
const confirmBtn = document.getElementById("confirmBtn");
const cancelBtn = document.getElementById("cancelBtn");
const elements = document.querySelectorAll('.delButton');
const searchBtn = document.getElementById("search-btn");
const searchKey = document.getElementById("search");

var QUESTIONCONTEXT;
var QUESTIONID;     

// 搜索函数
function searchQuestion(){
    event.preventDefault();  // 阻止表单的默认提交行为
    // 获取搜索框内的内容
    var QUESTIONCONTEXT = searchKey.value;
    // 向后端请求查询
    $.ajax({
        url: '/question/',
        type: 'GET',
        data:{
            'search_key': QUESTIONCONTEXT,
        },
        success: function(res){
            if (res.code == 'success'){
                // 进行展示搜索的题目
                console.dir(res.text);
            }else{
                alert("搜索失败");
            }
        }
    })
}

// 遍历元素，并为每个元素绑定点击事件监听器
elements.forEach(element => {
  element.addEventListener('click', clickDelQuestion);
  
});

// 提示信息
function showAlert(message) {
    const alertBox = document.getElementById("alertBox");
    alertBox.textContent = message;
    alertBox.classList.add("show");
  
    setTimeout(function () {
      alertBox.classList.remove("show");
      window.location.reload();
    }, 380);
    
  }

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
                // 显示提示信息
                showAlert("删除成功！");
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

// 绑定监听事件
function clickDelQuestion(){
    QUESTIONID = this.getAttribute('delId');   
    openModal();    // 打开模态框

}

// 绑定函数
confirmBtn.addEventListener("click", handleConfirmClick);
cancelBtn.addEventListener("click", handleCancelClick);

// 搜索按钮上绑定事件
searchBtn.addEventListener("click", searchQuestion);


