import asyncio

   # 非同期タスクA
async def async_task_a():
    print("非同期タスクA: 開始")
    await asyncio.sleep(2)  # 2秒間の待機
    print("非同期タスクA: 終了")

# 非同期タスクB
async def async_task_b():
    print("非同期タスクB: 開始")
    await asyncio.sleep(1)  # 1秒間の待機
    print("非同期タスクB: 終了")
    
def main():
    print("メイン関数: 開始")
    asyncio.run(async_main())
    print("メイン関数: 終了")
   

async def async_main():
    print("非同期関数: 開始")

    # 非同期タスクAとBを起動
    task_a = asyncio.create_task(async_task_a())
    task_b = asyncio.create_task(async_task_b())

    # 両方の非同期タスクの完了を待つ
    await task_a
    await task_b
    print("非同期関数: 終了")

main()

