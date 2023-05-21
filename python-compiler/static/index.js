$("#form").submit(function(e){
    e.preventDefault();
});

$('#code').keydown(function (e) {
    if(e.originalEvent.key == 'Tab')
    {
        e.preventDefault();
        console.log(e.selectionStart);
        var start = this.selectionStart;
        var end = this.selectionEnd;
    
        this.value = this.value.substring(0, start) +
          "\t" + this.value.substring(end);
    
        this.selectionStart =
          this.selectionEnd = start + 1;
    }
});

function send_ajax_request(){
    let data = $('#code').val();
   
    $.ajax({
        type : 'POST',
        url : '',
        data : {'csrfmiddlewaretoken': csrf , 'code': data ,'action':'execute_code'},
        success : function (result) {
            let output = result.output;
            console.log(result.output);
            $('#code_data').val(output);
        }
    })
}