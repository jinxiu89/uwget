/***
 * 时间选择器
 */
function runDatetimePicker(){
  $("#search-datetime-start").datetimepicker({
    language:  'zh-cn',
    format: 'yyyy-mm-dd hh:ii',
    minView: "month",
    todayBtn:  1,
    autoclose: 1,
    endDate : new Date(),
  }).on('changeDate', function(event) {
    event.preventDefault();
    event.stopPropagation();
    var startTime = event.date;
    $('#search-datetime-end').datetimepicker('setStartDate',startTime);
  });
  $("#search-datetime-end").datetimepicker({
    language:  'zh-cn',
    format: 'yyyy-mm-dd hh:ii',
    minView: "month",
    todayBtn:  1,
    autoclose: 1,
    endDate : new Date(),
  }).on('changeDate', function(event) {
    event.preventDefault();
    event.stopPropagation();
    var endTime = event.date;
    $("#search-datetime-start").datetimepicker('setEndDate',endTime);
  });
}
/*图片-添加*/
function add_640(title, url) {
    var index = layer.open({
        type: 2,
        title: title,
        area: ['630px', '360px'],
        content: url
    });
    layer.full(index);
}

/*弹出层*/

/*
	参数解释：
	title	标题
	url		请求的url
	id		需要操作的数据id
	w		弹出层宽度（缺省调默认值）
	h		弹出层高度（缺省调默认值）
*/
function layer_show(title, url, w, h) {
    if (title == null || title === '') {
        title = false;
    }
    if (url == null || url === '') {
        url = "404.html";
    }
    if (w == null || w === '') {
        w = 800;
    }
    if (h == null || h === '') {
        h = ($(window).height() - 50);
    }
    layer.open({
        type: 2,
        area: [w + 'px', h + 'px'],
        fix: false, //不固定
        maxmin: true,
        shade: 0.4,
        title: title,
        content: url
    });
}