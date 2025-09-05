local scale_factor = 2.7

function love.load()
    cam = require 'libraries/camera'
    camera = cam()
    cam_X = 0
    cam_Y = 0
    camera:lookAt(cam_X, cam_Y)

    canvas = love.graphics.newCanvas(800, 600)
    Canvas(canvas)

    --canvas:newImageData():encode("png","filename.png")
    
end



function love.draw()
    camera:attach()
        love.graphics.setBlendMode("alpha", "premultiplied")
        love.graphics.draw(canvas, -300, -300)
    camera:detach()

end


function Canvas(canvas)
    love.graphics.setCanvas(canvas)
        love.graphics.clear(0, 0, 0)

        local points = {}
        for x = 0, 600 do
            for y = 0, 600 do
                local ca = (x - 300)/100  /scale_factor  -0.6
                local cb = (y - 300)/100  /scale_factor  - 0
                local a = ca
                local b = cb
                local count = 0
                local bright = 0

                for n = 1, 100 do
                    count = count + 1
                    local aa = a^2  -  b^2
                    local bb = 2*a*b

                    a = aa + ca
                    b = bb + cb

                    if  math.abs(aa+bb) > 16  then
                        --bright = true
                        bright = n
                        break
                    end
                end

                table.insert(points, x*600 + y, {x, y, bright/100, bright/100, bright/100})

            end
        end
        love.graphics.points(points)

    love.graphics.setCanvas()
end





function love.keypressed(key)
    if key == "c" then
        love.graphics.captureScreenshot(os.time() .. ".png")
    end
end