import user_manager
import logging


logging.basicConfig(
    level=logging.DEBUG,
    filename='test.log',
    filemode='w'
)

if __name__ == "__main__":
    manager = user_manager.UserManager()
    logging.info("TEST CASE 1 (RF1)")

    manager.add_user(1, "Alice")

    logging.info('PASS using the debugger')

    logging.info("end test case 1")

    logging.info('TEST CASE 2 (RF2)')
    #manager.add_user(1, "Alice")
    manager.add_user(2, "Bob")
    manager.add_user(3, "Charlie")

    user1 = manager.find_user(2)
    logging.info('before if')
    if user1['name'] == 'Bob':
        logging.info('PASS')

    else:
        logging.info('FAIl')

    logging.info('TEST CASE 3')
    manager.delete_user(3)
    logging.info('PASS USING THE DEBUGGER')
    logging.info('end test case')

    logging.info('TEST CASE 4')
    all_names = manager.get_all_names()
    logging.info(f'The names are: {all_names}')
    if all_names == ['Alice', 'Bob']:
        logging.info('PASS')
    else:
        logging.error('FAIl')
        logging.warning('the function return the IDs')

    logging.info('TEST CASE 5 (RNF1)')

    for i in range (1000):
        manager.add_user(i, 'user'+str(i))
    logging.info('PASS using the debugger')

    logging.info('end TEST CASE')