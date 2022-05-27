function start_roll() {
    var speed = 30; // 可自行设置文字滚动的速度
    var wrapper = document.getElementById('risk_wrapper');
    var li1 = document.getElementById('risk_wrapper_li1');
    var li2 = document.getElementById('risk_wrapper_li2');
    li2.innerHTML = li1.innerHTML //克隆内容
    function Marquee() {
        if (li2.offsetHeight - wrapper.scrollTop <= 0) //当滚动至demo1与demo2交界时
            wrapper.scrollTop -= li1.offsetHeight //demo跳到最顶端
        else {
            wrapper.scrollTop++ //如果是横向的 将 所有的 height top 改成 width left
        }
    }
    var MyMar = setInterval(Marquee, speed) //设置定时器
    wrapper.onmouseover = function () {
        clearInterval(MyMar)    //鼠标移上时清除定时器达到滚动停止的目的
    }
    wrapper.onmouseout = function () {
        MyMar = setInterval(Marquee, speed)  //鼠标移开时重设定时器
    }
}