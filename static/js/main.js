$(function(){
	if ($.validator) {
		var main_form = $("#form").validate({
			rules: {
				title: {required: true}
			},
			errorPlacement: function (error, element){
				error.appendTo(element.siblings('ins'));
			},
			submitHandler: function (form) {
				debugger;
				$.ajax({
					url : form.action,
					type : "POST",
					data : $("#form").serialize(),

					success : function(json) {
						debugger;
						if (json.redirect){
							window.location = json.redirect;
						}else{
							window.location = '/';
						}

					},
					error : function(data) {
						data = data.responseJSON;
						for (var key in data) {
							var msg = data[key].join(' ');
							$('.'+key+'-error').text(msg);
						}
						$('.errors').html()
					}				 
				})
			},

			highlight: function (element, errorClass) {
				$(element).parent('.form-group').addClass('has-error').removeClass('check');
			},

			unhighlight: function (element, errorClass, validClass) {
				$(element).parent('.form-group').addClass('check').removeClass('has-error');
			},
		});
	}
});