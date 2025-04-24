import { DragDropContext } from 'react-beautiful-dnd';

const StrategyBuilder = ({ algorithms }) => {
  const [blocks, setBlocks] = useState([]);
  
  const onDragEnd = (result) => {
    if (!result.destination) return;
    const items = Array.from(blocks);
    const [reordered] = items.splice(result.source.index, 1);
    items.splice(result.destination.index, 0, reordered);
    setBlocks(items);
  };

  return (
    <DragDropContext onDragEnd={onDragEnd}>
      <Droppable droppableId="blocks">
        {/* Interactive blocks for RSI, MACD, on-chain triggers */}
      </Droppable>
    </DragDropContext>
  );
};
