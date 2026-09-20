import { useNavigate } from 'react-router-dom'
import { FaDumbbell, FaPen, FaChartLine } from 'react-icons/fa6'

function Home() {
  const navigate = useNavigate()

  return (
    <main className="home">
        <div className='home__container'>
            <div className='home__container_title'>Gym Tracker</div>

            <div className="home__container_menu">
                <button onClick={() => navigate('/training')}>
                <FaDumbbell />
                Treinar
                </button>

                <button onClick={() => navigate('/workouts')}>
                <FaPen />
                Criar / Editar Treino
                </button>

                <button onClick={() => navigate('/history')}>
                <FaChartLine />
                Histórico / Estatísticas
                </button>
            </div>
        </div>
    </main>
  )
}

export default Home