let vote_counts = [0, 0]
let fields_count = document.getElementById("answer_items").children.length;
let id_count = 1;
let elems;
if (!Element.prototype.remove) {
    Element.prototype.remove = function remove() {
        if (this.parentNode) {
            this.parentNode.removeChild(this);
        }
    };
}

function add_new_answer_field(value = '') {
    if(fields_count < 20){
        fields_count += 1;
        id_count += 1;
        vote_counts.push(0);
        var scrolled = window.pageYOffset;
        let child_elem = document.createElement("div");
        scrollDown(scrolled, 1);
        child_elem.id = "answer_element_" + String(id_count);
        child_elem.innerHTML = document.getElementById("answer_items").children[0].innerHTML;
        child_elem.children[1].setAttribute("delete_number", id_count);
        child_elem.children[1].id = "del_btn_" + id_count.toString();
        child_elem.children[0].value = value;
        answer_items.appendChild(child_elem);
    }
}

function scrollDown(endPos, i) {
    setTimeout(function () {
        if (parseInt(endPos) < $(document).height()) {
            var y = parseInt(endPos) + 1 * parseInt(i);
            window.scroll(0, y); //Устанавливаем новую позицию вертикального скрола
            scrollDown(y, parseInt(i) + 2);//Рекурсивный вызов функции
        }
    }, 10);

}

setInterval(function () {
    fields = document.getElementsByClassName("text_field");
    for (let i = 0; i < fields.length; i++) {
        if (fields[i].value.length == 0) {
            fields[i].style.border = "3px solid #d33342";
        }
        else {
            fields[i].style.border = "3px solid #72bb53";
        }
    }
    elems = document.getElementsByClassName("btn_delete");
    for (let i = 0; i < elems.length; i++) {
        let e = elems[i];
        e.onclick = function () {
            if (fields_count > 2) {
                let del_number = String(e.getAttribute("delete_number"));
                el = document.getElementById("answer_element_" + del_number);
                el.remove();
                vote_counts[del_number] = -1;
                fields_count--;
            }
        }
    }
}, 200);
