function auto_height(elementId) {
    obj = document.getElementById(elementId);
    obj.style.height = "auto";
    obj.style.height = (obj.scrollHeight + 10) + "px";
}

btn_clear = document.getElementById('btn-clear');
btn_clear.addEventListener('click', function () {
    gates_input = document.getElementById('logic-gates');
    gates_input.value = "";
    output = document.getElementById('output');
    output.value = "";
    graph = document.getElementById('graph');
    graph.value = "";
    auto_height('output');
    auto_height('graph');
});

btn_run = document.getElementById('btn-run');
btn_run.addEventListener('click', function () {
    let gates_string = document.getElementById('logic-gates').value;
    console.log(gates_string.split("\n"));
    let passed = true;
    let gates = gates_string.split("\n");
    let n_bits = gates[0].split(" ").length;
    for(let i = 0; i < gates.length; i++) {
        console.log(gates[i]);
        let components = gates[i].split(" ");
        if (components.length != n_bits) {
            alert("量子數長度不同，請重新輸入");
            passed = false;
            break;
        }
        for(let j = 0; j < components.length; j++) {
            if (parseInt(components[j]) > 3 || parseInt(components[j]) < 0) {
                alert("非合法邏輯閘單元，請重新輸入");
                passed = false;
                break;
            }
            if (components.filter(x => x==2).length > 1) {
                alert("單一邏輯閘內有多於一個NOT gate，請重新輸入");
                passed = false;
                break;
            }
        }
        if (!passed) {
            break;
        }
    }
    if (passed) {
        form = document.getElementById('gates-form');
        form.submit();
    }else {
        document.getElementById('logic-gates').value = "";
    }
})

auto_height('output');
auto_height('graph');