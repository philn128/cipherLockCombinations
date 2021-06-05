#!/usr/bin/env julia
#=
Efficient computation of partition numbers p(n) for n <= 405
and of arrays containing all partitions of a number n.
The array of partitions of 95 requires a little under 10GB of RAM.
=#

module Partitions
#partition numbers [p(0),p(1),...,p(n)]
#test: compare partn(49) to http://oeis.org/A000041/list
function partn(n)
    cache = Vector{Int64}(undef, n+1)
    for m in 0:n
        partn!(m, cache)
    end
    cache
end
    
#cache[n+1] = p(n) if cache[m+1] == p(m) for m < n
function partn!(n, cache)
    if n<=0
        cache[1] = 1
        return
    end
    #use pentagonal number theorem
    t, s, k = 0, 1, 1
    while true
        gk = pentagon(k)
        gk <= n || break
        t += s*cache[n - gk + 1]
        gk = pentagon(-k)
        gk <= n || break
        t += s*cache[n - gk + 1]
        s = -s
        k += 1
    end
    cache[n + 1] = t
end

pentagon(k) = ((3k-1)k)>>1

#=
Returns (P,partn(n)) where P contains the partitions of each m in 1:n.
For each m in 1:n and k in 1:p(m), one and only one prefix
of P[:,k] is a non-increasing sequence of positive integers with sum m.
For each m, these prefixes are exactly the partitions of m, 
listed in antilexicographic order without repetiton.
For each m < n, no prefix of P[:,p(m)+1] has sum m.
=#
function parts(n)
    L = partn(n)
    c = L[end]
    P = zeros(Int8, n, c)
    P[1,1] = 1
    b = 2
    for m in 1:n-1
        for a in 1:L[m+1]
            cum, i = 0, 1
            while true
                cum += P[i,a]
                cum < m || break
                i += 1
            end
            P[i+1,a] = 1
            if i<2 || P[i-1,a] > P[i,a] 
                for j in 1:i-1
                    P[j,b] = P[j,a]
                end
                P[i,b] = P[i,a] + 1
                b += 1
            end
        end
    end
    P,L
end

end #module

p8=Partitions.parts(8)
display(hcat(0:8,p8[2]))
println()
display(p8[1])
println()
