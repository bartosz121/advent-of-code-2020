function readFile()
    local file = io.open("input.txt", "r")
    local arr = {}
    for line in file:lines() do
        table.insert(arr, tonumber(line))
    end
    return arr
end

function part1(numbers)
    for _, v1 in pairs(numbers) do
        for _, v2 in pairs(numbers) do
            if v1+v2 == 2020 then
                return v1*v2
            end
        end
    end
    return -1
end


function part2(numbers)
    for _, v1 in pairs(numbers) do
        for _, v2 in pairs(numbers) do
            for _, v3 in pairs(numbers) do
                if v1+v2+v3 == 2020 then
                    return v1*v2*v3
                end
            end
        end
    end
    return -1
end

do
    local input = readFile()
    print(part1(input))
    print(part2(input))
end