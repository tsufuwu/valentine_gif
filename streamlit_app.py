import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Valentine's Proposal", page_icon="🌻", layout="wide")

# Hide Streamlit UI elements
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            .block-container {padding-top: 0; padding-left: 0; padding-right: 0; padding-bottom: 0;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Main HTML Content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Valentine's Proposal</title>
    <link href="https://fonts.googleapis.com/css2?family=Segoe+UI:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #FFE4E1;
            --text-color: #FF69B4;
            --yes-color: #98FB98;
            --no-color: #FF6B6B;
        }
        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        
        /* Proposal Screen */
        #proposal-screen {
            text-align: center;
            z-index: 10;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .title {
            color: var(--text-color);
            font-size: 2.5rem;
            margin-bottom: 3rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .buttons-container {
            display: flex;
            justify-content: center;
            gap: 2rem;
            align-items: center;
            position: relative;
            width: 100%;
            height: 100px;
        }
        button {
            padding: 15px 40px;
            font-size: 1.5rem;
            font-weight: bold;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        #yes-button {
            background-color: var(--yes-color);
            color: white;
            transition: transform 0.3s;
        }
        .glowing-effect {
            animation: glowing 1.5s infinite;
        }
        #no-button {
            background-color: var(--no-color);
            color: white;
            /* position: absolute; REMOVED to fix layout overlap */
            transition: top 0.2s, left 0.2s; /* Smooth movement when running away */
        }
        
        /* Sunflower Screen */
        #sunflower-screen {
            display: none; /* Hidden initially */
            width: 100%;
            height: 100%;
            position: relative;
            justify-content: center;
            align-items: flex-start;
            padding-top: 50px;
        }
        .success-message {
            color: white;
            font-size: 2rem; /* Reduced from 3rem */
            text-align: center;
            z-index: 10;
            text-shadow: 0 0 10px #FF69B4, 0 0 20px #FF69B4;
            animation: fadeIn 2s ease-in;
            margin-top: 20px;
        }
        canvas {
            position: absolute;
            top: 0;
            left: 0;
            z-index: -1;
        }
        
        /* Animations */
        @keyframes glowing {
            0% { box-shadow: 0 0 5px #98FB98, 0 0 10px #98FB98; }
            50% { box-shadow: 0 0 20px #98FB98, 0 0 30px #98FB98; }
            100% { box-shadow: 0 0 5px #98FB98, 0 0 10px #98FB98; }
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes floatGif {
            0% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0); }
        }
        
        .gif-decoration {
            position: absolute;
            width: 100px; /* Reduced from 150px */
            height: auto;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(255, 105, 180, 0.5);
            z-index: 5;
            opacity: 0; /* Start hidden */
        }
        
        /* Gift Button */
        #gift-button {
            position: absolute;
            top: 50%; /* Vertically centered */
            left: 10%; /* Aligned with left GIFs */
            transform: translateY(-50%);
            background-color: #FF1493;
            color: white;
            z-index: 20;
            border: 2px solid white;
            font-size: 1rem;
            padding: 10px 25px;
            opacity: 0;
            animation: fadeIn 1s ease-out 8s forwards, glowing 1.5s infinite 8s;
        }
        #gift-button:hover {
            transform: translateY(-50%) scale(1.1);
            background-color: #C71585;
        }

        /* Modal */
        #video-modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-color: rgba(0, 0, 0, 0.85);
            justify-content: center;
            align-items: center;
            z-index: 100;
            animation: fadeIn 0.3s ease-out;
        }
        .video-modal-content {
            position: relative;
            background: transparent;
            padding: 0;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(255, 105, 180, 0.5);
        }
        .close-modal {
            position: absolute;
            top: -40px;
            right: -40px;
            background: transparent;
            color: white;
            font-size: 2rem;
            border: none;
            cursor: pointer;
            padding: 10px;
            line-height: 1;
        }
    </style>
</head>
<body>

    <!-- Proposal Screen -->
    <div id="proposal-screen">
        <h1 class="title">Yuno có tha thứ cho Tsufu vì đã bảo Yuno ăn nhiều không?</h1>
        <div class="buttons-container">
            <button id="yes-button" class="glowing-effect" onclick="acceptProposal()">YES</button>
            <button id="no-button" onmouseenter="runAway()" onclick="runAway()">NO</button>
        </div>
    </div>

    <!-- Sunflower Screen -->
    <div id="sunflower-screen">
        <h1 class="success-message">Hì hì, cảm ơn Yuno ❤️<br>Valentine vui vẻ🌻</h1>
        <canvas id="sunflower-canvas"></canvas>
        
        <!-- GIFs -->
        <!-- Note: Using raw.githubusercontent.com links -->
        <img src="https://raw.githubusercontent.com/tsufuwu/valentine_gif/main/web-app/src/assets/Art%20Love%20GIF%20by%20Cosytales.gif" 
             class="gif-decoration" 
             style="top: 20%; left: 10%; animation: fadeIn 1s ease-out 4s forwards, floatGif 3s ease-in-out infinite 4s;">
             
        <img src="https://raw.githubusercontent.com/tsufuwu/valentine_gif/main/web-app/src/assets/anime-valentines-day.gif" 
             class="gif-decoration" 
             style="bottom: 20%; right: 10%; animation: fadeIn 1s ease-out 5s forwards, floatGif 3s ease-in-out infinite 5s;">
             
        <img src="https://raw.githubusercontent.com/tsufuwu/valentine_gif/main/web-app/src/assets/be-mine-valentine.gif" 
             class="gif-decoration" 
             style="top: 20%; right: 10%; animation: fadeIn 1s ease-out 6s forwards, floatGif 3s ease-in-out infinite 6s;">
             
        <img src="https://raw.githubusercontent.com/tsufuwu/valentine_gif/main/web-app/src/assets/feeding-anime-cute.gif" 
             class="gif-decoration" 
             style="bottom: 20%; left: 10%; animation: fadeIn 1s ease-out 7s forwards, floatGif 3s ease-in-out infinite 7s;">

        <button id="gift-button" onclick="showGift()">Nhận quà Valentine 🎁</button>

        <div id="video-modal" onclick="closeGift()">
            <div class="video-modal-content" onclick="event.stopPropagation()">
                <button class="close-modal" onclick="closeGift()">×</button>
                <iframe 
                    src="https://drive.google.com/file/d/1etQn0_2zm9uD_bksF_OTi3uKR-YZZiVz/preview" 
                    width="640" 
                    height="480" 
                    allow="autoplay"
                    style="border: none; border-radius: 10px; max-width: 100%; max-height: 80vh;"
                ></iframe>
            </div>
        </div>
    </div>

    <script>
        // Proposal Logic
        let yesScale = 1;
        
        function runAway() {
            yesScale += 0.5;
            document.getElementById('yes-button').style.transform = `scale(${yesScale})`;
            
            const btn = document.getElementById('no-button');
            const maxOffsetX = window.innerWidth / 2 - 100;
            const maxOffsetY = window.innerHeight / 2 - 100;
            
            // Random position from center, but we need absolute positioning relative to container or body?
            // The CSS says absolute. position: absolute relative to... body (if container is static)
            // But buttons-container is flex. Wait, no-button style says position: absolute.
            // Let's set top/left relative to window center for simplicity or stick to container?
            // Actually, keep it simple: Fixed position coordinates or percentage.
            
            const x = (Math.random() * maxOffsetX * 2) - maxOffsetX;
            const y = (Math.random() * maxOffsetY * 2) - maxOffsetY;
            
            // We need to set it relative to the center of the screen
            // But 'absolute' inside a flexible container is tricky.
            // Let's change no-button to fixed position when it starts moving?
            btn.style.position = 'fixed';
            btn.style.left = `calc(50% + ${x}px)`;
            btn.style.top = `calc(50% + ${y}px)`;
        }

        function acceptProposal() {
            document.getElementById('proposal-screen').style.display = 'none';
            document.getElementById('sunflower-screen').style.display = 'flex'; // Use flex to center text?
            // Actually sunflower-screen styles: display: none initially.
            
            // Start sunflower animation
            setTimeout(startSunflower, 2000); // 2s delay
        }

        // Sunflower Logic
        function startSunflower() {
            const canvas = document.getElementById('sunflower-canvas');
            const ctx = canvas.getContext('2d');
            
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            
            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2;
            
            // Background
            ctx.fillStyle = 'black';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // Draw Leaves
            function drawLeaf(angle) {
                ctx.save();
                ctx.translate(centerX, centerY + 70); // Moved up (was 100)
                ctx.rotate(angle * Math.PI / 180);
                ctx.beginPath();
                ctx.fillStyle = '#FFA216';
                ctx.ellipse(0, -90, 25, 90, 0, 0, 2 * Math.PI); // Slightly smaller leaf
                ctx.fill();
                ctx.restore();
            }
            
            for(let i=0; i<16; i++) {
                drawLeaf(i * (360/16));
            }
            
            // Draw Center
            const goldenAngle = 137.508;
            function drawCenter(i) {
                if (i > 140) return;
                
                const r = 3.5 * Math.sqrt(i) * 5; // Reduced scale (was 4)
                const theta = i * goldenAngle * (Math.PI / 180);
                const x = centerX + r * Math.cos(theta);
                const y = centerY + r * Math.sin(theta);
                
                ctx.beginPath();
                ctx.arc(x, y, 3, 0, 2 * Math.PI); // Smaller seeds
                ctx.fillStyle = '#8B4513';
                ctx.fill();
                
                requestAnimationFrame(() => drawCenter(i + 1));
            }
            
            drawCenter(0);
        }

        // Modal Logic
        function showGift() {
            document.getElementById('video-modal').style.display = 'flex';
        }
        
        function closeGift() {
            document.getElementById('video-modal').style.display = 'none';
        }
    </script>
</body>
</html>
"""

# Render the HTML
components.html(html_content, height=800, scrolling=False)
