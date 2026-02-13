import { useState } from 'react';

interface ProposalProps {
    onAccept: () => void;
}

const Proposal = ({ onAccept }: ProposalProps) => {
    const [yesScale, setYesScale] = useState(1);
    const [noPosition, setNoPosition] = useState({ x: 0, y: 0 });

    const handleNoRunAway = () => {
        setYesScale(prev => prev + 0.5);
        // Calculate random position within the viewport, ensuring it stays visible and nearby
        const maxOffsetX = window.innerWidth / 2 - 100; // Safe horizontal limit
        const maxOffsetY = window.innerHeight / 2 - 100; // Safe vertical limit

        // Generate random x/y between -maxOffset and +maxOffset
        const newX = (Math.random() * maxOffsetX * 2) - maxOffsetX;
        const newY = (Math.random() * maxOffsetY * 2) - maxOffsetY;

        // Optionally, make it less jittery by limiting the max jump distance if needed,
        // but for now, just ensure it's within bounds.
        setNoPosition({ x: newX, y: newY });
    };

    return (
        <div className="proposal-container">
            <h1 className="title">Yuno có tha thứ cho Tsufu vì đã bảo Yuno ăn nhiều không?</h1>
            <div className="buttons-container">
                <button
                    className="yes-button glowing-effect"
                    style={{ transform: `scale(${yesScale})` }}
                    onClick={onAccept}
                >
                    YES
                </button>
                <button
                    className="no-button"
                    style={{ transform: `translate(${noPosition.x}px, ${noPosition.y}px)` }}
                    onMouseEnter={handleNoRunAway}
                    onClick={handleNoRunAway}
                >
                    NO
                </button>
            </div>
        </div>
    );
};

export default Proposal;
