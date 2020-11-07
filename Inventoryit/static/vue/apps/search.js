new Vue({
    el: '#app',
    delimiters: ['{$', '$}'],
 
   data:{
        kword:'',
        list_inv:[]
   },
   watch:{
    kword: function (val) {
        this.search(val);
    }
   },
   methods: { 
        search: function (kword) {
            var self = this;
            axios.get('/api/search/list/?kword=' + kword)
            .then(function (response){
                self.list_inv = response.data
            
            })
            .catch(function(error){
                console.log(error)
            })
        },
        

    },


});
