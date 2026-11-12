#!/usr/bin/lua

function f(n)
    if n < 0 then
        return n
    end
    if n == 0 then
        return 1
    else
        return n * f(n - 1)
    end
end

print("Enter a number:")
local a = io.read("*n")

print(f(a))
