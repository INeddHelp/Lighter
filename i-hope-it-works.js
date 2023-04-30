const readline = require('readline')
const fs = require('fs')
const path = require('path')
const math = require('mathjs')

function lighter () {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  })

  rl.question(
    'Enter a file to split (or type "exit" to stop): ',
    function (input) {
      if (input.toLowerCase() === 'exit') {
        rl.close()
        return
      }

      if (fs.existsSync(input)) {
        const fileStat = fs.statSync(input)
        if (fileStat.isFile()) {
          const file_size = fileStat.size
          if (file_size <= 100 * 1024 * 1024) {
            console.log(input)
          } else {
            const {
              dir: fileDir,
              name: fileName,
              ext: fileExt
            } = path.parse(input)
            const num_parts = math.ceil(file_size / (100 * 1024 * 1024))
            const dir_name = `${fileName}_parts`
            fs.mkdirSync(dir_name, { recursive: true })
            const fileData = fs.readFileSync(input)
            for (let i = 0; i < num_parts; i++) {
              const part_path = path.join(
                dir_name,
                `${fileName}_part${i + 1}${fileExt}`
              )
              const partData = fileData.slice(
                i * 100 * 1024 * 1024,
                (i + 1) * 100 * 1024 * 1024
              )
              fs.writeFileSync(part_path, partData)
              console.log(part_path)
            }
          }
        } else {
          console.log(`Not a file: ${input}`)
        }
      } else {
        console.log(`File not found: ${input}`)
      }

      lighter()
    }
  )
}

lighter()
