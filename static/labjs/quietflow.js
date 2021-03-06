function randCol(a, o, e, r) {
    return "rgba(" + Math.floor(Math.random() * a).toString() + "," + Math.floor(Math.random() * o).toString() + "," + Math.floor(Math.random() * e).toString() + "," + r + ")"
}
$.fn.quietflow = function (a) {
    function o(a) {
        void 0 !== x.speed ? setTimeout(function () {
            w = requestAnimationFrame(a)
        }, x.speed) : w = requestAnimationFrame(a)
    }

    function e() {
        for (var a = 0; h > a; a += x.squareSize + 1)
            for (var r = 0; c > r; r += x.squareSize + 1) S.fillStyle = randCol(x.maxRed, x.maxGreen, x.maxBlue, 1), S.fillRect(a, r, x.squareSize, x.squareSize);
        o(e)
    }

    function r() {
        (B + y > h || 0 > B + y) && (y = -y), (F + k > c || 0 > F + k) && (k = -k), B += y, F += k, S.fillStyle = x.backgroundCol, S.fillRect(0, 0, h, c);
        for (var a = 0; a < x.miniRadii; a++)
            for (var e = 0; e < x.miniRadii; e++) {
                var t = a / x.miniRadii * h,
                    l = e / x.miniRadii * c,
                    i = Math.sqrt(Math.pow(B - t, 2) + Math.pow(F - l, 2)) / x.mainRadius;
                S.beginPath(), S.fillStyle = x.circleCol, S.arc(t, l, i, 0, 2 * Math.PI, !0), S.closePath(), S.fill()
            }
        o(r)
    }

    function t() {
        S.fillStyle = x.backgroundCol, S.fillRect(0, 0, h, c);
        for (var a = 0; a < x.bounceBallCount; a++) {
            var e = circleData[a],
                r = 0,
                l = 1,
                i = 2,
                n = 3,
                s = 4,
                d = 5;
            (e[r] + e[n] > h || e[r] + e[n] < 0) && (e[3] = -e[3]), (e[l] + e[s] > c || e[l] + e[s] < 0) && (e[s] = -e[s]), e[r] += e[n], e[l] += e[s], S.beginPath(), S.fillStyle = e[d], S.arc(e[r], e[l], e[i], 0, 2 * Math.PI, !0), S.closePath(), S.fill()
        }
        o(t)
    }

    function l() {
        S.fillStyle = x.backgroundCol, S.fillRect(0, 0, h, c), S.beginPath(), S.fillStyle = x.lineColor, S.arc(f, m, 2, 0, 2 * Math.PI, !0), S.closePath(), S.fill();
        for (var a = 0; a < x.lines; a++) S.beginPath(), S.moveTo(f, m), S.lineTo(Math.random() * h, Math.random() * c), S.strokeStyle = x.lineColor, S.shadowColor = x.lineGlow, S.shadowBlur = 20, S.stroke();
        o(l)
    }

    function i() {
        var a = S.createLinearGradient(0, 0, h / 2, c);
        a.addColorStop(0, "#333333"), a.addColorStop(1, "#000"), S.fillStyle = a, S.fillRect(0, 0, h, c);
        for (var e = 0; e < P.length; e++) {
            var r = P[e],
                t = 0,
                l = 1,
                n = 2,
                s = 3;
            r[t] += r[s], S.beginPath(), S.fillStyle = x.starColor, S.arc(r[t], r[l], r[n], 0, 2 * Math.PI, !0), S.shadowColor = "#FFF", S.shadowBlur = 20, S.closePath(), S.fill(), r[t] > h && (P.splice(e, 1), P.unshift([Math.random() * h / 4 - h / 4, Math.random() * c, Math.random() * x.starSize, Math.ceil(5 * Math.random())]))
        }
        o(i)
    }

    function n() {
        S.beginPath();
        for (var a = [
            [0, 0],
            [h, 0],
            [0, c],
            [h, c]
        ], e = 0; 4 > e; e++) {
            var r = Math.floor(Math.random() * x.specificColors.length);
            S.strokeStyle = x.specificColors.length > 0 ? x.specificColors[r] : randCol(255, 255, 255), S.moveTo(a[e][0], a[e][1]), S.lineTo(Math.random() * h, Math.random() * c)
        }
        S.shadowColor = x.lineGlow, S.shadowBlur = 20, S.stroke(), o(n)
    }

    function s() {
        S.fillStyle = x.backgroundCol, S.fillRect(0, 0, h, c);
        for (var a = 0; a < q.length; a++) {
            var e = q[a],
                r = 0,
                t = 1,
                l = 2,
                i = 3,
                n = 4;
            S.fillStyle = e[i], S.fillRect(e[r], e[t], e[l], e[l]), e[r] += e[n], e[t] -= e[n], (e[r] > h + x.maxBoxSize || e[t] < -x.maxBoxSize) && (q.splice(a, 1), 0 == x.specificColors.length ? q.push([Math.random() * h * 2 - h, Math.random() * c * 2 + c, Math.random() * x.maxBoxSize + 1, randCol(255, 255, 255, x.transparent ? .5 : 1), 5 * Math.random()]) : q.push([Math.random() * h * 2 - h, Math.random() * c * 2 + c, Math.random() * x.maxBoxSize + 1, x.specificColors[Math.floor(Math.random() * x.specificColors.length)], 5 * Math.random()]))
        }
        o(s)
    }
    var d = $(this),
        h = d.width(),
        c = d.height(),
        f = h / 2,
        m = c / 2;
    $("#Quietflow").remove();
    var u = "starfield",
        M = -1e3,
        p = ["squareFlash", "vortex", "bouncingBalls", "shootingLines", "simpleGradient", "starfield", "layeredTriangles", "cornerSpikes", "floatingBoxes"],
        C = {
            squareFlash: {
                squareSize: 10,
                maxRed: 255,
                maxGreen: 255,
                maxBlue: 255,
                speed: 100
            },
            vortex: {
                mainRadius: 20,
                miniRadii: 30,
                backgroundCol: "#3498DB",
                circleCol: "#34495E",
                speed: 10
            },
            bouncingBalls: {
                specificColors: [],
                backgroundCol: "#ECF0F1",
                maxRadius: 40,
                bounceSpeed: 50,
                bounceBallCount: 50,
                transparent: !0
            },
            shootingLines: {
                backgroundCol: "#000",
                lineColor: "#FFF",
                speed: 150,
                lineGlow: "#FFF",
                lines: 50
            },
            simpleGradient: {
                primary: "#D4145A",
                accent: "#FBB03B"
            },
            starfield: {
                starColor: "#FFF",
                starSize: 3,
                speed: 100
            },
            layeredTriangles: {
                backgroundCol: "#D6D6D6",
                transparent: !0,
                specificColors: [],
                triangles: 50
            },
            cornerSpikes: {
                specificColors: [],
                backgroundCol: "#FFF",
                lineColor: "#000",
                speed: 100,
                lineGlow: "#FFF"
            },
            floatingBoxes: {
                specificColors: [],
                boxCount: 400,
                maxBoxSize: 80,
                backgroundCol: "#D6D6D6",
                transparent: !1,
                speed: 100
            }
        },
        g = document.createElement("canvas"),
        S = g.getContext("2d");
        // S.fillStyle = "green";
        // S.fillRect(0, 0, g.width, g.height);

    g.id = "Quietflow", g.width = h, g.height = c, g.style.zIndex = M, g.style.position = "absolute", g.style.top = 0;
    var b = d.attr("id");
    if (void 0 != b) {
        var v = document.getElementById(b);
        v.appendChild(g)
    } else document.body.appendChild(g);
    $.inArray(a.theme, p) > -1 && (u = a.theme);
    var x = {};
    x = $.extend(C[u], a), $(window).resize(function () {
        h = d.width(), c = d.height();
        var a = $("#Quietflow").css("width").replace("px", ""),
            o = $("#Quietflow").css("height").replace("px", "");
        $("#Quietflow").css({
            width: window.innerWidth,
            height: window.innerHeight
        });
        var e = a / window.innerWidth,
            r = o / window.innerHeight;
        S.scale(e, r)
    });
    var w;
    switch (u) {
    case "squareFlash":
        e();
        break;
    case "vortex":
        var y = 2,
            k = 4,
            B = h / 2,
            F = c / 2;
        r();
        break;
    case "bouncingBalls":
        circleData = [];
        for (var R = 0; R < x.bounceBallCount; R++) 0 == x.specificColors.length ? circleData.push([Math.random() * h, Math.random() * c, Math.random() * x.maxRadius, 2 * Math.random(), 4 * Math.random(), randCol(255, 255, 255, x.transparent ? .5 : 1)]) : circleData.push([Math.random() * h, Math.random() * c, Math.random() * x.maxRadius, 2 * Math.random(), 4 * Math.random(), x.specificColors[Math.floor(Math.random() * x.specificColors.length)]]);
        t();
        break;
    case "shootingLines":
        l();
        break;
    case "simpleGradient":
        var z = S.createLinearGradient(0, 0, h / 2, c);
        z.addColorStop(0, x.primary), z.addColorStop(1, x.accent), S.fillStyle = z, S.fillRect(0, 0, h, c);
        break;
    case "starfield":
        for (var P = [], R = 0; 700 > R; R++) P.push([Math.random() * h * 2 - h, Math.random() * c, Math.random() * x.starSize, Math.ceil(5 * Math.random())]);
        i();
        break;
    case "layeredTriangles":
        S.fillStyle = x.backgroundCol, S.fillRect(0, 0, h, c);
        for (var R = 0; R < x.triangles; R++) S.beginPath(), S.moveTo(Math.random() * h, Math.random() * c), S.lineTo(Math.random() * h, Math.random() * c), S.lineTo(Math.random() * h, Math.random() * c), x.specificColors.length > 0 ? S.fillStyle = x.specificColors[Math.floor(Math.random() * x.specificColors.length)] : S.fillStyle = randCol(255, 255, 255, .5), S.closePath(), S.fill();
        break;
    case "cornerSpikes":
        S.fillStyle = x.backgroundCol, S.fillRect(0, 0, h, c), n();
        break;
    case "floatingBoxes":
        for (var q = [], R = 0; R < x.boxCount; R++) 0 == x.specificColors.length ? q.push([Math.random() * h * 2 - h, Math.random() * c, Math.random() * x.maxBoxSize + 1, randCol(255, 255, 255, x.transparent ? .5 : 1), 5 * Math.random()]) : q.push([Math.random() * h * 2 - h, Math.random() * c, Math.random() * x.maxBoxSize + 1, x.specificColors[Math.floor(Math.random() * x.specificColors.length)], 5 * Math.random()]);
        s()
    }
};