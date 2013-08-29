(function($,$S){
    if (typeof $S.Organization == 'undefined'){
        $S.Organization = {};
    }

    $S.Organization.create = function(){
        var name = $("#name").val();
        var phone = $("#phone").val();
        var url = '/manage/organization/list';
        var method = 'POST';
        var data = {'name': name, 'phone': phone};
        var status = {'success': '添加成功', 'org_name_exist': '该组织已存在'};
        $S.ajax(url, method, {'data': data, 'status': status});
    };

    $S.Organization.addManager = function(id){
        var email = $("#org-"+id).val();
        var url = '/manage/organization/' + id + '/manager';
        var method = 'POST';
        var data = {'email': email};
        var status = {'success': '添加管理员成功', 'email_not_exist': '该邮箱不存在'};
        $S.ajax(url, method, {'data':data, 'status': status});
    };

    $S.Organization.remove = function(id){
        var url = '/manage/organization/' + id;
        var method = 'DELETE';
        var status = {'success': '删除成功', 'org_not_exist': '组织不存在'};
        $S.ajax(url, method, {'status': status});
    };

})(jQuery, StuCampus);
