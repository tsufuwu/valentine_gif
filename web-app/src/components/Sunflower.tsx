import { useEffect, useRef, useState } from 'react';
import artLoveGif from '../assets/Art Love GIF by Cosytales.gif';
import animeValGif from '../assets/anime-valentines-day.gif';
import beMineGif from '../assets/be-mine-valentine.gif';
import feedingGif from '../assets/feeding-anime-cute.gif';

const Sunflower = () => {
    const canvasRef = useRef<HTMLCanvasElement>(null);
    const [showVideo, setShowVideo] = useState(false);

    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        if (!ctx) return;

        // Set canvas size to window size
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        // Animation constants
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;

        // Draw background
        ctx.fillStyle = 'black';
        ctx.fillRect(0, 0, canvas.width, canvas.height);



        // Draw Leaves
        const drawLeaf = (angle: number) => {
            ctx.save();
            ctx.translate(centerX, centerY + 100); // Move down a bit
            ctx.rotate(angle * Math.PI / 180);

            ctx.beginPath();
            ctx.fillStyle = '#FFA216';
            // Simplified leaf shape for canvas
            ctx.ellipse(0, -100, 30, 100, 0, 0, 2 * Math.PI);
            ctx.fill();
            ctx.restore();
        };

        // Draw multiple leaves
        for (let i = 0; i < 16; i++) {
            drawLeaf(i * (360 / 16));
        }


        // Draw Flower Center (Phyllotaxis)
        const goldenAngle = 137.508;
        const drawCenter = (i: number) => {
            if (i > 140) return; // Stop after 140 seeds

            const r = 4 * Math.sqrt(i) * 5; // Scale up for visibility
            const theta = i * goldenAngle * (Math.PI / 180);

            const x = centerX + r * Math.cos(theta);
            const y = centerY + r * Math.sin(theta); // Moved up to center of leaves

            ctx.beginPath();
            ctx.arc(x, y, 4, 0, 2 * Math.PI);
            ctx.fillStyle = '#8B4513';
            ctx.fill();

            requestAnimationFrame(() => drawCenter(i + 1));
        };

        // Start drawing center animation - Delayed by 2s
        const timer = setTimeout(() => {
            drawCenter(0);
        }, 2000); // Wait for text to fade in

        return () => clearTimeout(timer);
    }, []);

    return (
        <div className="sunflower-container">
            <h1 className="success-message">Hì hì, cảm ơn Yuno ❤️<br />Valentine vui vẻ🌻</h1>

            {/* Display GIFs around the flower - Sequenced */}
            <img
                src={artLoveGif}
                alt="Love Art"
                className="gif-decoration"
                style={{
                    top: '20%',
                    left: '10%',
                    animation: 'fadeIn 1s ease-out 4s forwards, floatGif 3s ease-in-out infinite 4s'
                }}
            />
            <img
                src={animeValGif}
                alt="Anime Valentine"
                className="gif-decoration"
                style={{
                    bottom: '20%',
                    right: '10%',
                    animation: 'fadeIn 1s ease-out 5s forwards, floatGif 3s ease-in-out infinite 5s'
                }}
            />
            <img
                src={beMineGif}
                alt="Be Mine"
                className="gif-decoration"
                style={{
                    top: '20%',
                    right: '10%',
                    animation: 'fadeIn 1s ease-out 6s forwards, floatGif 3s ease-in-out infinite 6s'
                }}
            />
            <img
                src={feedingGif}
                alt="Feeding Cute"
                className="gif-decoration"
                style={{
                    bottom: '20%',
                    left: '10%',
                    animation: 'fadeIn 1s ease-out 7s forwards, floatGif 3s ease-in-out infinite 7s'
                }}
            />

            {/* Gift Button */}
            <button
                className="gift-button"
                onClick={() => setShowVideo(true)}
            >
                Nhận quà Valentine 🎁
            </button>


            {/* Video Modal */}
            {showVideo && (
                <div className="video-modal-overlay" onClick={() => setShowVideo(false)}>
                    <div className="video-modal-content" onClick={e => e.stopPropagation()}>
                        <button className="close-modal" onClick={() => setShowVideo(false)}>×</button>
                        <iframe
                            src="https://drive.google.com/file/d/1etQn0_2zm9uD_bksF_OTi3uKR-YZZiVz/preview"
                            width="640"
                            height="480"
                            allow="autoplay"
                            style={{ border: 'none', borderRadius: '10px', maxWidth: '100%', maxHeight: '80vh' }}
                        ></iframe>
                    </div>
                </div>
            )}

            <canvas ref={canvasRef} style={{ position: 'absolute', top: 0, left: 0, zIndex: -1 }} />
        </div>
    );
};

export default Sunflower;
