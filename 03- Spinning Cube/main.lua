function love.load()
    require("2D_LinearAlgebra")

    cam = require 'libraries/camera'
    camera = cam()
    camera:lookAt(0, 0)



    points = {}
    points[1] = {-50, -50, -50}
    points[2] = {50, -50, -50}
    points[3] = {50, 50, -50}
    points[4] = {-50, 50, -50}
    points[5] = {-50, -50, 50}
    points[6] = {50, -50, 50}
    points[7] = {50, 50, 50}
    points[8] = {-50, 50, 50}


    rotated = {}


    theta = 0

    RotationX = {
        {1, 0, 0},
        {0, math.cos(theta), -math.sin(theta)},
        {0, math.sin(theta), math.cos(theta)}
    }

    RotationY = {
        {math.cos(theta), 0, math.sin(theta)},
        {0, 1, 0},
        {-math.sin(theta), 0, math.cos(theta)}
    }

    RotationZ = {
        {math.cos(theta), -math.sin(theta), 0},
        {math.sin(theta), math.cos(theta), 0},
        {0, 0, 1}
    }
end



function love.update(dt)
    theta = theta + 0.03

    RotationX = {
        {1, 0, 0},
        {0, math.cos(theta), -math.sin(theta)},
        {0, math.sin(theta), math.cos(theta)}
    }

    RotationY = {
        {math.cos(theta), 0, math.sin(theta)},
        {0, 1, 0},
        {-math.sin(theta), 0, math.cos(theta)}
    }

    RotationZ = {
        {math.cos(theta), -math.sin(theta), 0},
        {math.sin(theta), math.cos(theta), 0},
        {0, 0, 1}
    }

    for n = 1, #points do
        rotated[n] = {}
        rotated[n] = LinAlg.Mult(RotationX, points[n])
        rotated[n] = LinAlg.Mult(RotationY, rotated[n])
        rotated[n] = LinAlg.Mult(RotationZ, rotated[n])
    end
end



function love.draw()
    camera:attach()
        love.graphics.setPointSize(6)
        for n = 1, #rotated do
            love.graphics.points( rotated[n][1], rotated[n][2] )
        end

        love.graphics.line( rotated[1][1], rotated[1][2], rotated[2][1], rotated[2][2])
        love.graphics.line( rotated[2][1], rotated[2][2], rotated[3][1], rotated[3][2])
        love.graphics.line( rotated[3][1], rotated[3][2], rotated[4][1], rotated[4][2])
        love.graphics.line( rotated[4][1], rotated[4][2], rotated[1][1], rotated[1][2])

        love.graphics.line( rotated[5][1], rotated[5][2], rotated[6][1], rotated[6][2])
        love.graphics.line( rotated[6][1], rotated[6][2], rotated[7][1], rotated[7][2])
        love.graphics.line( rotated[7][1], rotated[7][2], rotated[8][1], rotated[8][2])
        love.graphics.line( rotated[8][1], rotated[8][2], rotated[5][1], rotated[5][2])

        love.graphics.line( rotated[1][1], rotated[1][2], rotated[5][1], rotated[5][2])
        love.graphics.line( rotated[2][1], rotated[2][2], rotated[6][1], rotated[6][2])
        love.graphics.line( rotated[3][1], rotated[3][2], rotated[7][1], rotated[7][2])
        love.graphics.line( rotated[4][1], rotated[4][2], rotated[8][1], rotated[8][2])



    camera:detach()

    love.graphics.print(tostring(love.getVersion()), 10, 10)
end