function AreYouSureModal({ setIsModalVisible }) {
    const handleCloseModal = () => {
        setIsModalVisible(false);
      }

    return <div className='are-you-sure-modal'>
      <p>Desaja {} o perfil?</p>
      <button
      >
        Sim
      </button>
      <button
        onClick={handleCloseModal}
      >
        Não
      </button>
    </div>
}

export default AreYouSureModal;