
def multiTable(n: Int): String = {
    var table = ""
    var multiplo = 1
    while multiplo < 11 do
        if multiplo < 10 then
            table += s"$multiplo * $n = " + multiplo * n + "\n"
        else
            table += s"$multiplo * $n = " + multiplo * n
        multiplo += 1
    return table
}
