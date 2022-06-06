// script 

console.log("hello")


var checkb = document.querySelectorAll('.checkbox1');
console.log(checkb)


sum1 = 0;
sum2 = 0;
checkb.forEach((check, index) => {
    check.addEventListener('click', function () {

        if (this.checked == true) {

            var table = document.getElementById("table1");
            sum1 = sum1 + parseInt(table.rows[index + 1].cells[2].innerHTML);
            sum2 = sum2 + parseInt(table.rows[index + 1].cells[1].innerHTML);
            first()
        }
        else if (this.checked != true) {
            var table = document.getElementById("table1");
            sum1 = sum1 - parseInt(table.rows[index + 1].cells[2].innerHTML);
            sum2 = sum2 - parseInt(table.rows[index + 1].cells[1].innerHTML);
            first()
        }
        else {
            sum1 = 0;
            sum2 = 0;
            document.getElementById('selected').innerHTML = sumval;
        }
    })
})


var checkb = document.querySelectorAll('.checkbox2');
console.log(checkb)


sum3 = 0;
sum4 = 0;
checkb.forEach((check, index) => {
    check.addEventListener('click', function () {
        if (this.checked == true) {

            var table = document.getElementById("table2");
            sum3 = sum3 + parseInt(table.rows[index + 1].cells[2].innerHTML);
            sum4 = sum4 + parseInt(table.rows[index + 1].cells[1].innerHTML);
            first()
        }
        else if (this.checked != true) {
            var table = document.getElementById("table2");
            sum3 = sum3 - parseInt(table.rows[index + 1].cells[2].innerHTML);
            sum4 = sum4 - parseInt(table.rows[index + 1].cells[1].innerHTML);
            first()
        }
        else {
            sum2 = 0;
            document.getElementById('selected').innerHTML = sum2;
        }
    })
})

function first() {
    debit = sum1 - sum3;
    credit = sum2 - sum4
    document.getElementById('selected').innerHTML = debit;
    document.getElementById('selected2').innerHTML = credit;
}
