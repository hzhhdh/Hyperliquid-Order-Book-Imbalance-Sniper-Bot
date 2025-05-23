import { createLogger, format, transports } from 'winston';
const logger = createLogger({
  level: 'info',
  format: format.combine(format.timestamp(), format.json()),
  transports: [new transports.File({ filename: 'cryptostake.log' })],
});
export function logInfo(message: string): void {
  logger.info(message);
}
