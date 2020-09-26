
function add( ){
        $('#basicExampleModal').modal('show')
}
function clean_up(){
        $("#id_sap_id").val("")
        $("#id_internet_host_names").val("")
        $("#id_loopback").val("")
        $("#id_mac_address").val("")
        $("#id_id").val("")
}
function delete_data(r){
var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        if(confirm("Are you sure??"))
             $.ajax({
                    method:"delete",
                    headers:{"X-CSRFToken": $crf_token},
                    url: "/rest-api/"+r+"/",
                    success: handleFormSuccess.bind(this ) ,
                    error: handleFormError,
                    })

        }

  $(document).ready(function(){
           dt =  $('#router-detail').DataTable({
              'serverSide': true,
              'ajax': 'http://localhost:8000/rest-api/?format=datatables',
               'columns': [
                {'data': 'id'},
                  {'data': 'sap_id'},
                  {'data': 'internet_host_names' },
                  {'data': 'loopback'},
                  {'data': 'mac_address'},
                   {
                    data: null,
                    className: "center",
                    defaultContent: '<a href="" class="editor_edit">Edit</a> / <a href="" class="editor_remove">Delete</a>'
                  }
              ]

          });
           $('#router-detail').on('click', 'a.editor_remove', function (e) {
            e.preventDefault();
             var  tr= $(this).closest('tr')
             delete_data(tr.children()[0].innerText)
           })
      $('#router-detail').on('click', 'a.editor_edit', function (e) {
        e.preventDefault();
            var  tr= $(this).closest('tr')
             $("#id_id").val(tr.children()[0].innerText)
            $("#id_sap_id").val(tr.children()[1].innerText)
            $("#id_internet_host_names").val(tr.children()[2].innerText)
            $("#id_loopback").val(tr.children()[3].innerText)
            $("#id_mac_address").val(tr.children()[4].innerText)


            $('#basicExampleModal').modal('show')
        } );
        $("#basicExampleModal").on('hide.bs.modal', function(){
            clean_up()
            console.log("Clean up")
        });

        $('#update_data').click( function() {

            sap_id = $("#id_sap_id").val( ).trim()
            internet_host_names = $("#id_internet_host_names").val( ).trim()
            loopback = $("#id_loopback").val( ).trim()
            mac_address = $("#id_mac_address").val( ).trim()
            id= $("#id_id").val( ).trim()
            var formData = { sap_id,internet_host_names,loopback,mac_address}
            var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
            data_url = id == ""?"/rest-api/":"/rest-api/"+id+"/"
            method_type = id == ""?"POST":"PUT"
            $.ajax({
                method:method_type,
                headers:{"X-CSRFToken": $crf_token},
                url: data_url,
                data: formData,
                success: handleFormSuccess.bind(this ) ,
                error: handleFormError,
                })
            })
})
 function handleFormSuccess( data, response,textStatus, jqXHR){

        $('#basicExampleModal').modal('hide')
        dt.ajax.reload();
    }

    function handleFormError(jqXHR, textStatus, errorThrown){
         alert(jqXHR.responseText)
        console.log(jqXHR)
        console.log(textStatus)
        console.log(errorThrown)
    }
