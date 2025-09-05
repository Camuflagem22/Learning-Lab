LinAlg = {}


function LinAlg.Vec_Add(a, b)               -- tested and working
    if #a ~= #b then
        return nil
    end

    result = {}
    for n = 1, #a do
        result[n] = a[n] + b[n]
    end

    return result

end


function LinAlg.Vec_Sub(a, b)               -- tested and working
    if #a ~= #b then
        return nil
    end

    result = {}
    for n = 1, #a do
        result[n] = a[n] - b[n]
    end

    return result

end


function LinAlg.Vec_Dot(a, b)
    if #a ~= #b then
        return nil
    end

    result = 0
    for n = 1, #a do
        result =  result + (a[n] * b[n])
    end

    return result

end


function LinAlg.Vec_Scale(lambda, vec)
    for n = 1, #vec do
        vec[n] =  vec[n] * lambda
    end
    return vec
end


-- This is a Linear Transformation
function LinAlg.Mult(A, B)
    if #A[1] ~= #B then
        return nil
    end

    Result = {}
    for i = 1, #A do
        
        Result[i] = 0
        for j = 1, #A[i] do
            Result[i] = Result[i] + (A[i][j] * B[j])
        end
    end

    return Result
end


return vector